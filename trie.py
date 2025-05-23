class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
        
    def insert(self, word):
        node = self.root
        print(node)
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word_end = True
         
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word_end
    def start_with(self, prefix):
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True
    
    def count_words_start_with(self, prefix):
        def dfs(node):
            count = 1 if node.is_word_end else 0
            for child in node.children.values():
                count += dfs(child)
            return count

        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return dfs(node)

    def delete(self, word):
        def _delete(node, word, depth):
            if depth == len(word):
                if not node.is_word_end:
                    return False  # Word not found
                node.is_word_end = False
                return len(node.children) == 0  # If leaf, delete this node

            char = word[depth]
            if char not in node.children:
                return False
            should_delete = _delete(node.children[char], word, depth + 1)

            if should_delete:
                del node.children[char]
                return len(node.children) == 0 and not node.is_word_end
            return False

        _delete(self.root, word, 0)

    def longest_common_prefix(self):
        prefix = ""
        node = self.root
        while node and len(node.children) == 1 and not node.is_word_end:
            char = next(iter(node.children))
            prefix += char
            node = node.children[char]
        return prefix

# Example usage
trie = Trie()
trie.insert("hello")
trie.insert("world")

# Search for 'hello' in the trie
result = trie.search("hello")
print(result)  # Output: True

# Search for 'world' in the trie
result = trie.search("world")
print(result)  # Output: True

print(trie.start_with('h'))