# 535. Encode and Decode TinyURL
# Difficulty: Medium
# https://leetcode.com/problems/encode-and-decode-tinyurl/

import random
import string

DOMAIN = "http://tinyurl.com/"

class Codec:
    
    slug_to_url = {}
    
    def encode(self, long_url: str) -> str:
        """Encodes a URL to a shortened URL.
        """        
        lowercase_letters = random.choices(string.ascii_lowercase, k=3)
        uppercase_letters = random.choices(string.ascii_uppercase, k=3)
        numerals = random.choices(string.digits, k=2)
        
        random_chars = lowercase_letters + uppercase_letters + numerals
        random.shuffle(random_chars)

        slug = "".join(random_chars)        
        self.slug_to_url[slug] = long_url
        
        return DOMAIN + slug
        

    def decode(self, short_url: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        slug = short_url.replace(DOMAIN, "")

        return self.slug_to_url.get(slug)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))