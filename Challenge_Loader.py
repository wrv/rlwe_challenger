import Challenges_pb2 as chal_proto

challenge = chal_proto.Challenge()
challengeInstance = chal_proto.InstanceCont()

try:
	toyEx1File = open("challenges\\chall-id0000-rlwec-m256-q769-l3-short-toy\\chall-id0000-rlwec-m256-q769-l3-short-toy.challenge", 'rb')
	toyEx1InstFile = open("challenges\\chall-id0000-rlwec-m256-q769-l3-short-toy\\chall-id0000-rlwec-m256-q769-l3-short-toy-10.instance", 'rb')
	challenge.ParseFromString(toyEx1File.read())
	challengeInstance.ParseFromString(toyEx1InstFile.read())
	toyEx1File.close()
except IOError:
	print "could not open file"

print "First challenge instance in toy: "
aVals =  challengeInstance.samples[0].a
bVals = challengeInstance.samples[0].b
m =  aVals.m
q = aVals.q

print "\tm value: " + str(m)
print "\tq value: " + str(q)

print "\tSamples (a, b=a*s+e): " + str(len(aVals.xs)) + " samples"
if len(aVals.xs) == len(bVals.xs):
	for j in range(len(aVals.xs)):
		print "\t(" + str(aVals.xs[j]) + "," + str(bVals.xs[j]) + ")"