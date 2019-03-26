#!/usr/bin/python

# Script: getCloudMetric.py 
# Creator: daniel.soto@linkeit.com
# Abstract: Este script permite recuperar cualquier metrica desde CloudWatch
#           utilizando la biblioteca boto3.
#           Se calcula el timestamp actual y el timestamp correspondiente
#           al 'rangeTime' especificado para recuperar los DataPoints de 
#           la metrica que queremos recuperar. Se calcula la media de todos los 
#           valores recuperados.

import boto3
import datetime
import sys

region = 'eu-west-1'
rangeTime = 1200
period = 300

cw = boto3.client('cloudwatch', region_name = region)

#Checking the amount of arguments used

if len(sys.argv) != 6:
	print "Some arguments are missing: python cloudwatch_metrics.py Namespace MetricName DimensionName DimensionValue Statistic"
else: 
	namespace = sys.argv[1] # e.g. 'AWS/RDS'
	metricname = sys.argv[2] # e.g. CPUUtilization
	dimname = sys.argv[3] # e.g. DBInstanceIdentifier
	dimvalue = sys.argv[4] # e.g. MyDB
	statistic = sys.argv[5] # [ Sum, Maximum, Minimum, SampleCount, Average ]
	try:
		metric = cw.get_metric_statistics(
	        Namespace = namespace,
	        MetricName = metricname,
	        Dimensions = [
	        				{
	        					'Name': dimname,
	        			 		'Value': dimvalue
	        			 	}

	        			 ],
	        # Obtenemos los valores del estadistico especificado para todos los Datapoints
		# entre las fechas especificadas.
	        
		StartTime = datetime.datetime.utcnow() - datetime.timedelta(seconds = rangeTime),
	        EndTime = datetime.datetime.utcnow(),
	        Period = period,
	        Statistics = [statistic]
	   )	
		#print "Valor obtenido de los Datapoints entre:"
		#print datetime.datetime.utcnow() - datetime.timedelta(seconds = period)
		#print datetime.datetime.utcnow()

		# Obtenemos los valores de los estadisticos de los diferentes DataPoints
		# y calculamos el valor medio.

		statisticValues = []
		for data in metric['Datapoints']:
			statisticValues.append(data[statistic])

		print sum(statisticValues) / float(len(statisticValues))
	except Exception, e:
		print e


