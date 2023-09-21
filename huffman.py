import heapq
from collections import Counter


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    char_freq = Counter(text)
    priority_queue = [Node(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def build_huffman_codes(node, current_code="", codes=None):
    if codes is None:
        codes = {}
    if node is not None:
        if node.char is not None:
            codes[node.char] = current_code
        build_huffman_codes(node.left, current_code + "0", codes)
        build_huffman_codes(node.right, current_code + "1", codes)
    return codes

def huffman_encode(text):
    root = build_huffman_tree(text)

    codes = build_huffman_codes(root)
    encoded_text = "".join(codes[char] for char in text)
    print(codes)
    return encoded_text



with open('input.txt', 'r') as file:
    input_string = file.read()

    encoded_result = huffman_encode(input_string)

    with open('output.txt', 'w') as output:
        output.write(encoded_result)
    print(encoded_result)


