# Fine tune LLM Model
## Quantization
1. Full precision/Half Precision -> Data -> Weight and parameter
2. Calibration -> model Quantization -> problem
3. Modes of Quantization -> Post training Qauantization, Quantization Aware Training

# Quantization:
Defination: Conversion from higher memory format to lower memory format
Any neural network, when train the NN. What parameters. Weights are usually in matrix. 3*3 matrix. every values store in memory in 32 bits. like FP32. floating point 32. it is full precision/single precision.

7.23 store in 32 bit memory. If you have very big LLM like lemma 70 billion parameeter. Then require fine tuning. I can not directly download in local system. It isnot posible
Other wise take private cloud network but lot of cost is involved. Why 70 bilion because very weight.
So We can convert this 32 bit into int 8 the download. Thenwe do inferencing. 

this become quite easy. We are converting it into highr memory format into low memory format.

Specific deep leaning model in mobile phone. This time I can do quatize. or any edge device.

Trying to lower down memory. FP32 -> FP16 bit. This is quantization
It is half precision

Tensorflow also do this. TF32 bit.

Main aim is bigger model to lower model with better unferecing purpose. with help of quantization.

Whe we perform quantization there is loss of infromation.

## what exactly is calibration
What is math formula? Two types of quantization
1. Symmteric quantization -> batch normalization. ie.e entire weight of ditrbution is cenetred 
near zero.
Ex. One technique: Symmetric unsint8 qauntilzation
suppose one floting point no.
1 to 10000 -> weight of larger model ->LLM model -> 32 bits
Now convert thisinto unsigned 8 bit -> 2^8 ie convert from 0 to 1000 to 2 to 255
Single point Floating point 32.
sign + exponent + mantissa ()

FP 16. : 1bit sign + 5 bit exponent+ 10 bit Mantissa

min max scalar: How we convert this no in 
0.0 -> 0
1000 -> 255

Scale formula:
scale = Xmax-xmin/qmax - qmin= 1000-0/255-0=3.92
This is scale factor.  

2. Assymetric uint8 quantization:
in case of no is not symmtricaly dotributed.
zero point=5
This two parameter require for quantization.

## 2. Calibration
Squzing process is called calibration

### Post training qualtization: PTQ
We have pretrained model. basically weight are very high.We apply
Pretrained  model -> calibration->quantized model -> use cases

## Quantization aware technique : QAT
Tjere is loss of data. so accuracy decrese. 
Trained model-> quantization -> finetunnig

With help of PTQ loss of data is there. But there is new training data.

### PART 2:
LORA: Low Order Rank Adaptation:
This is specfific used ofr fine tuning of LLM application.
Wheerever there is pretrained LLM model. This model trained with huge amount of data. All this model. Like so many token, 
GPT 4, GPT Turbo
Further there are varuous ways of fine tuning. This fine tuning done all weights of these variables.
We can say full parameter finiding. We use this model and domain specific fine tuning. It ca be dofferent different araes.
Anothe is specific task fine tuning. ex. Q and A chatbot, text to sql, like

#### Full paramater fine tuning.
What are challges in full paramater fine tuning. I have google 170 biloin  weight. When we fine tuning we updates weight. Therr is hardware constraint. For downstream task it si very difficult like model minnitoring, model inferecngin, gpu ocntaint, RAM containt, we have many challages
Use use LORA and Clora 

#### Lora
what it will Do? 
Instead of updating all weight, it will track the changes of new weight based on fine tuning.

Pretarined weight + LoRA tarined weight = Fine tuned weight
There is tech is matric decompostion happen. 3*1 * 1*3 = 3*3

I am getting all 9 weight from 6 parameters
Bigger matrix converted into two smaller matrix which solve the resouce contarint.
W0 + delta W = Wo + B A

what happen if increseing rank. but parameres remain less require

### Clora
float 16 bit->4 bit -> 16 bit

### Practical
Parameter-Efficient Transfer Leaning for NLP










2. Assymetric quantization



