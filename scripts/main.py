import os
import yaml
import praw
import pickle
import time

from paths import paths

class main:

    def load_creds(self):
        root_path = self.paths.root
        with open(root_path + "/secrets.yaml", 'r') as file:
            self.secrets = yaml.safe_load(file)
    
    def load_mods(self):
        root_path = self.paths.root
        with open(root_path + "/mod_list.yaml", 'r') as file:
            self.mod_list = yaml.safe_load(file)
    
    def load_log_comments(self):
        root_path = self.paths.root
        if 'log_comments' not in os.listdir(root_path):
            self.log_comments = {}
            for mod in self.mod_list:
                self.log_comments[mod] = []
            self.save_log_comments()
        else:
            with open(root_path + "/log_comments", 'rb') as handle:
                self.log_comments = pickle.load(handle)
    
    def save_log_comments(self):
        for mod in self.mod_list:
            if self.log_comments.get(mod) == None:
                self.log_comments[mod] = []
            if len(self.log_comments.get(mod)) > 5:
                self.log_comments[mod] = self.log_comments[mod][0:5]
        root_path = self.paths.root
        with open(root_path + "/log_comments", 'wb') as handle:
            pickle.dump(self.log_comments, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def load_reddit(self):
        self.reddit = praw.Reddit(client_id=self.secrets['CLIENT_ID'],
                     client_secret=self.secrets['CLIENT_SECRET'],
                     user_agent=self.secrets['USER_AGENT'],
                     username=self.secrets['username'],
                     password=self.secrets['password'])
    
    def get_comments(self, username):
        return self.reddit.redditor(username).comments.new(limit=self.comment_limit)

    def __init__(self):
        self.paths = paths()
        self.load_creds()
        self.load_reddit()
        self.load_mods()

        self.comment_limit = 5
        self.load_log_comments()
        
        while(True):
            for mod in self.mod_list:
                print("shaming mod " + str(mod))
                comments = self.get_comments(mod)
                for comment in comments:
                    # print(comment.body)
                    if comment.id not in self.log_comments[mod]:
                        try:
                            comment.reply('Just trying out a bot. :D')
                            self.log_comments[mod].append(comment.id)
                            print('shamed')
                        except:
                            print("some dipshit error")
            self.save_log_comments()
            print("sleeping")
            time.sleep(5)

if __name__ == '__main__':
    main = main()