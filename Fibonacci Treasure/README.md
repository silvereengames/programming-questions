# **Fibonacci Treasure**  

## **Problem Statement**  
Captain Blackbeard has found a set of numbers carved into the side of an ancient shipwreck. The legendary navigator, Old Man Barnacle, believes these numbers hold the secret to a lost treasure, but only if they follow a hidden pattern.  

The rule is simple: Every **other** number in the sequence must belong to the **Fibonacci sequence**. If they do, the numbers reveal the way to the treasure. If not, they are just a decoy left by rival pirates.  

Your task is to determine if the given sequence follows this rule:  
- Read an integer **n**, representing the number of numbers in the sequence.  
- Read **n** integers and check if every **second number** (starting from the **second position, index 1**) is a Fibonacci number.  
- If all these numbers belong to the Fibonacci sequence, print `"I love me numbers!"`. Otherwise, print `"These numbers suck!"`.  

Can you crack the code and help Blackbeard find his treasure, or will you be fooled by a false trail?  

---  

## **Input**  
Each test case consists of two lines:  
- The first line contains an integer **n** (1 ≤ n ≤ 10⁵) — the number of numbers in the sequence.  
- The second line contains **n** space-separated integers.  

It is guaranteed that the absolute value of the numbers does not exceed **10⁹**.  

---  

## **Output**  
Print `"I love me numbers!"` if every second number (starting from index **1**) is a Fibonacci number. Otherwise, print `"These numbers suck!"`.  

---  

## **Example**  

### **Input**  
```
12  
72 0 86 1 90 1 89 2 67 3 74 5  
```  

### **Output**  
```
I love me numbers!  
```  

---  

### **Input**  
```
10  
81 0 98 2 73 4 87 98 26 102  
```  

### **Output**  
```
These numbers suck!  
```  

Old Man Barnacle is counting on you—solve the mystery before Blackbeard makes you swab the deck! 🏴‍☠️💀