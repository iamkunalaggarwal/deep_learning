# inputs for model
inputs = [1,2.3,4.5,5.2,3.4]
#weights 
weights = [4.3,2,5,6.2,3]
# bias
bias = 4

output = 0

for i in len(inputs):
    outputs += inputs[i]*weights[i]
output+=bias

print("out for one layer cnn of 5 nodes: "+output)
