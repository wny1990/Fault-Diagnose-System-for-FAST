from django.db import models


class FaultMode(models.Model):
 
	FaultModeID = models.IntegerField(editable=False, default=0)
	FaultMode = models.CharField(max_length=200)
	FaultDescription= models.CharField(max_length=200)
	DetectionMethod = models.BooleanField()
	ManualDetectionMethodID = models.CharField(max_length=15)
	FunctionID = models.CharField(max_length=15)
	Priority = models.IntegerField()
	LogicalRelationship = models.BooleanField()

class FaultCause(models.Model):
	
	FaultCauseID = models.IntegerField(editable=False, default=0)
	FaultCause = models.CharField(max_length=15)
	FaultCauseDescription= models.CharField(max_length=200)
	HighLevelFaultModeID = models.CharField(max_length=15)
	DetectionMethod = models.BooleanField()
	ManualDetectionMethodID = models.CharField(max_length=15)
 	FunctionID = models.CharField(max_length=15)
	Priority = models.IntegerField()
	LogicalRelationship = models.BooleanField()
	MaintenanceSuggestions = models.CharField(max_length=300)

class FaultModeRelation(models.Model):

	HighLevelFaultModeID = models.IntegerField(editable=False, default=0)
	FaultModeID = models.CharField(max_length=15)
	LogicalRelationship = models.BooleanField()

class FaultCauseRelation(models.Model):

	FaultModeID = models.IntegerField(editable=False, default=0)
	FaultCauseID =  models.IntegerField(editable=False, default=0)
	LogicalRelationship = models.BooleanField()

'''
class FaultRelation(models.Model):

	FaultModeID = models.IntegerField(editable=False, default=0)
	FaultCauseID = models.CharField(max_length=15)
	LogicalRelationship = models.BooleanField()
'''

class ManualDetection(models.Model):

	ManualDetectionMethodID = models.CharField(max_length=15)
	MethodDescription= models.CharField(max_length=200)

class AutoDetection(models.Model):

	FunctionID = models.CharField(max_length=15)
	FunctionName = models.CharField(max_length=15)
	LogicalExp= models.CharField(max_length=200)

class FunctionArg(models.Model):
	
	FunctionID = models.CharField(max_length=15)
	ArgID = models.CharField(max_length=15)

class FunctionArgDes(models.Model):

	ArgID = models.CharField(max_length=15)
	ArgName = models.CharField(max_length=200)
	ArgDescription = models.CharField(max_length=200)
