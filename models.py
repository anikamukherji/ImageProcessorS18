from pymodm import fields, MongoModel

class User(MongoModel):
	email = fields.EmailField(primary_key=True) # because primary_key is True, we will need to query this field using the label _id
	hist_times = fields.IntegerField() # the number of times to do histogram
	contrast_times = fields.IntegerField()
	log_times = fields.IntegerField()
	reverse_times = fields.IntegerField()
	upload_time = fields.ListField(field=fields.DateTimeField())
	hist_time = fields.ListField(field=fields.DateTimeField())
	contrast_time = fields.ListField(field=fields.DateTimeField())
	log_times = fields.ListField(field=fields.DateTimeField())
	reverse_times = fields.ListField(field=fields.DateTimeField())
	image = fields.ListField(field=fields.CharField()())

	class Meta:
		write_concern = WriteConcern(j=True)
        	connection_alias = 'image-app'
