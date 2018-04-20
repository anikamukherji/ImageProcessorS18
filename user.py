from pymodm import connect
import models
import datetime

def create_user(email,hist_times,contrast_times,log_times,reverse_times):
	user = models.User(email,hist_times,contrast_times,log_times,reverse_times)
	u.save()

