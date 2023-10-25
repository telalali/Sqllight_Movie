from dataclasses import dataclass

@dataclass
class Category:
    id:int = 0
    name:str = ""
        
@dataclass
class Movie:
    id:int = 0
    name:str = ""
    year:int = 0
    minutes:int = 0
    desc:str = ""
    director: str = ""  # New field
    rating: float = 0.0  # New field
    cover_image: str = ""  # New field
    category:Category = None
    
    
