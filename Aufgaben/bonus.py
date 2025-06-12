import random
import math
import matplotlib.pyplot as plt
import numpy as np

unitCount = 3
sampleCount = 70

weightsA = [random.uniform(-1, 1) for _ in range(unitCount)]
weightsB = [[random.uniform(-1, 1)] for _ in range(unitCount)]

errorHistory = []

inputs = [(i / 10) for i in range(sampleCount)]
validationInputs = [(i / 10) + 0.05 for i in range(sampleCount)]

stepSize = 0.05
iterationCount = 15000

biasA = [random.uniform(-1, 1) for _ in range(unitCount)]
biasB = random.uniform(-1, 1)

def activation(x, factor=1):
    return 1 / (1 + math.exp(-factor * x))

def runTraining(cycles):
    global biasB
    totalDeviation = 0
    for cycle in range(cycles):
        for i in range(len(inputs)):
            tempLayer = [activation(inputs[i] * weightsA[j] + biasA[j]) for j in range(len(weightsA))]
            result = sum(tempLayer[j] * weightsB[j][0] for j in range(len(weightsB))) + biasB

            delta = math.sin(inputs[i]) - result
            totalDeviation += abs(delta)
            if i == len(inputs) - 1:
                errorHistory.append(totalDeviation / len(inputs))
                totalDeviation = 0

            for j in range(len(weightsA)):
                weightsA[j] += -stepSize * (-2 * delta * weightsB[j][0] * tempLayer[j] * (1 - tempLayer[j]) * inputs[i])
                biasA[j] += -stepSize * (-2 * delta * weightsB[j][0] * tempLayer[j] * (1 - tempLayer[j]))
            for j in range(len(weightsB)):
                weightsB[j][0] += -stepSize * (-2 * delta * tempLayer[j])
                biasB += -stepSize * (-2 * delta)
        if cycle % 100 == 0:
            print(str((cycle / cycles) * 100) + "%")

def evaluate(x):
    intermediate = [activation(x * weightsA[i] + biasA[i]) for i in range(len(weightsA))]
    result = sum(intermediate[i] * weightsB[i][0] for i in range(unitCount)) + biasB
    return result

def generateEstimation():
    return [evaluate(x) for x in inputs]

def generateReference():
    return [math.sin(x) for x in inputs]

print("Vor dem Training:")
print("Gewichte A: ", weightsA)
print("Gewichte B: ", weightsB)
print("Bias A: ", biasA)
print("Bias B: ", biasB)

runTraining(iterationCount)

print("Nach dem Training:")
print("Gewichte A: ", weightsA)
print("Gewichte B: ", weightsB)
print("Bias A: ", biasA)
print("Bias B: ", biasB)

estimated = generateEstimation()
reference = generateReference()

plt.figure(1)
plt.plot(inputs, estimated, label='Berechnet')
plt.plot(inputs, reference, label='Referenz')
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.title('Vergleich berechneter Werte')
plt.legend()

plt.figure(2)
plt.plot(range(0, iterationCount), errorHistory, label='Abweichung')
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.title('Fehlerverlauf')
plt.legend()

plt.show()
