from pymodm import fields, MongoModel


class User(MongoModel):
    username = fields.CharField(primary_key=True)
    hist_times = fields.IntegerField()
    contrast_times = fields.IntegerField()
    log_times = fields.IntegerField()
    reverse_times = fields.IntegerField()
    upload_time = fields.ListField(field=fields.DateTimeField())
    hist_time = fields.ListField(field=fields.DateTimeField())
    contrast_time = fields.ListField(field=fields.DateTimeField())
    log_time = fields.ListField(field=fields.DateTimeField())
    reverse_time = fields.ListField(field=fields.DateTimeField())
    image_original = fields.ListField(field=fields.CharField())
    image_hist = fields.ListField(field=fields.CharField())
    image_contrast = fields.ListField(field=fields.CharField())
    image_log = fields.ListField(field=fields.CharField())
    image_reverse = fields.ListField(field=fields.CharField())

    def vals(self):
        """
        Returns dictionary of attributes for object
        :return: dictionary of attributes
        :rtype: dict
        """
        vals = {
                "username": self.username,
                "user_upload_image": self.image_original,
                "hist_times": self.hist_times,
                "contrast_times": self.contrast_times,
                "log_times": self.log_times,
                "reverse_times": self.reverse_times,
                "upload_time": self.upload_time
                }
        return vals
