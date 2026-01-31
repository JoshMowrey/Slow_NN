import random


class slow_nn():
    def __init__(self, inputParams: int, outputParams: int, hiddenLayers: int = 0, hiddenParams: int = 0):
        self.inputParams = inputParams;
        self.outputParams = outputParams;
        self.hiddenLayers = hiddenLayers;
        self.hiddenParams = hiddenParams;

        self.layers = list();
        if (hiddenLayers == 0):
            self.layers.append(slow_layer(inputParams, outputParams));
            return;

        self.layers.append(slow_layer(inputParams, hiddenParams));
        for _ in range(hiddenLayers-1):
            self.layers.append(slow_layer(hiddenParams, hiddenParams));
        self.layers.append(slow_layer(hiddenParams, hiddenParams));

    def Eval(self, input: list):
        last = input;
        for layer in self.layers:
            last = layer.Eval(last);
        return last;


class slow_layer():
    def __init__(self, input: int, output: int):
        self.inputParams = input;
        self.outputParams = output;

        self.connections = list();
        if (input == 0 or output == 0):
            return;
        for i in range(input):
            self.connections.append(list());
            for _ in range(output):
                self.connections[i].append(random.random());

        

    
    def Eval(self, input: list):
        out = list();
        for i in self.connections:
            if (len(i) == 0):
                continue;
            sum = 0;
            for j in i:
                sum += input[i.index(j)] * j
            out.append(sum/len(i))
        return out;


                


