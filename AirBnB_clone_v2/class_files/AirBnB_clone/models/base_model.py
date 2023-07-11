#!/usr/bin/python3
"""
A CLASS BaseModel that defines all common attributes/method for other classes
"""
from datetime import datetime
import uuid


class BaseModel:
	"""
		A CLASS BaseModel that defines all common attributes/method for other classes
	"""

	def __init__(self, *args, **kwargs):
		"""
		Inittializing our Class
		"""
		if len(kwargs) < 1:
			id = str(uuid.uuid4())
			created_at = datetime.now()
			update_at = datetime.now()
			self.id = id
			self.created_at = created_at
			self.update_at = update_at
		else:
			for key, value in kwargs.items():
				if key != "__class__":
					if key == "created_at" or key == "update_at":
						value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
					setattr(self, key, value)	

	def __str__(self):
		"""This is a magic method that converts objects to human readable 
		string in this format:
		[<class name>] (<self.id>) <self.__dict__>
		"""
		return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

	def save(self):
		"""updates the public instance attribute updated_at with the
		current datetime"""
		self.updated_at = datetime.now()
		return self.updated_at
	
	def to_dict(self):
		"""returns a dictionary containing all keys/values of __dict__ of the instance"""
		our_dict = self.__dict__.copy()
		our_dict.update({"created_at": str(datetime.now().isoformat()), "__class__": self.__class__.__name__})
		return our_dict
