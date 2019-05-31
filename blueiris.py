import requests, json, hashlib, sys, argparse

class BlueIris:

    session = None

    response = None

    signals = ['red', 'green', 'yellow']



    def __init__(self, proto, host, user, password, debug=False):

        self.host = host

        self.user = user

        self.password = password
        
        self.proto = proto

        self.debug = debug

        self.url = proto+"://"+host+"/json"
        
        r = requests.post(self.url, data=json.dumps({"cmd":"login"}), verify=False)

        if r.status_code != 200:

            print( r.status_code)

            print( r.text)

            #sys.exit(1)



        self.session = r.json()["session"]
 

        self.response = hashlib.md5(('%s:%s:%s' % (user, self.session, password)).encode('utf-8')).hexdigest()
        if self.debug:

            print( "session: %s response: %s" % (self.session, self.response))

        r = requests.post(self.url, verify=False, data=json.dumps({"cmd":"login", "session": self.session, "response": self.response}))

        if r.status_code != 200 or r.json()["result"] != "success":

            print( r.status_code)

            print( r.text)

            sys.exit(1)

        self.system_name = r.json()["data"]["system name"]

        self.profiles_list = r.json()["data"]["profiles"]



#        print ("Connected to '%s'" % self.system_name)



    def cmd(self, cmd, params=dict()):

        args = {"session": self.session, "response": self.response, "cmd": cmd}

        args.update(params)



        # print( self.url)

        # print( "Sending Data: ")

        # print json.dumps(args)

        r = requests.post(self.url, verify=False, data=json.dumps(args))



        if r.status_code != 200:

            print (r.status_code)

            print (r.text)

            sys.exit(1)

        else:

            pass

            #print "success: " + str(r.status_code)

            #print r.text



        if self.debug:

            print (str(r.json()))



        try:

            return r.json()["data"]

        except:

            return r.json()



    def get_profile(self):

        r = self.cmd("status")

        profile_id = int(r["profile"])

        if profile_id == -1:

            return "Undefined"

        return self.profiles_list[profile_id]



    def get_signal(self):

        r = self.cmd("status")

        signal_id = int(r["signal"])

        return self.signals[signal_id]



    def get_schedule(self):

        r = self.cmd("status")

        schedule = r["schedule"]

        return schedule



    def set_signal(self, signal_name):

        signal_id = self.signals.index(signal_name)

        self.cmd("status", {"signal": signal_id})



    def set_schedule(self, schedule_name):

        self.cmd("status", {"schedule": schedule_name})



    def logout(self):

        self.cmd("logout")



if __name__ == "__main__":

    main()
