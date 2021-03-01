import numpy as np
import math
def calculate(list):
  if len(list)!=9:
     raise ValueError('List must contain nine numbers.')
  # clacultate the flattened metrics
  reshaped_list=np.reshape(list,(3,3))
  flattened_metrics=[]
  flattened_vector=reshaped_list.flatten()
  flattened_metrics.append(flattened_vector.mean())
  variance=np.var(flattened_vector)
  flattened_metrics.append(variance)
  flattened_metrics.append(math.sqrt(variance))
  flattened_metrics.append(flattened_vector.max())
  flattened_metrics.append(flattened_vector.min())
  flattened_metrics.append(flattened_vector.sum())

  #calculate axis1
  axis1_metrics=[]

  for i in range(3):
    axis1_metrics.append(reshaped_list[i,:].mean())
    variance=np.var(reshaped_list[i,:])
    axis1_metrics.append(variance)
    axis1_metrics.append(math.sqrt(variance))
    axis1_metrics.append(reshaped_list[i,:].max())
    axis1_metrics.append(reshaped_list[i,:].min())
    axis1_metrics.append(reshaped_list[i,:].sum())
 
  
  #calculate axis2
  axis2_metrics=[]

  for i in range(3):
    axis2_metrics.append(reshaped_list[:,i].mean())
    variance=np.var(reshaped_list[:,i])
    axis2_metrics.append(variance)
    axis2_metrics.append(math.sqrt(variance))
    axis2_metrics.append(reshaped_list[:,i].max())
    axis2_metrics.append(reshaped_list[:,i].min())
    axis2_metrics.append(reshaped_list[:,i].sum())

    #creating the dictionary
    calculations = {'mean': [axis1_metrics[0],axis2_metrics[0],flattened_metrics[0]],
    'variance':[axis1_metrics[1],axis2_metrics[1],flattened_metrics[1]],
    'standard deviation':[axis1_metrics[2],axis2_metrics[2],flattened_metrics[2]],
    'max':[axis1_metrics[3],axis2_metrics[3],flattened_metrics[3]],'min':[axis1_metrics[4],axis2_metrics[4],flattened_metrics[4]],'sum':[axis1_metrics[5],axis2_metrics[5],flattened_metrics[5]]
    }
 

  




    return calculations