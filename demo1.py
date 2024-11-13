import pandas as pd
import random

# List of unique names (200 unique names)
names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry", "Ivy", "Jack",
         "Kara", "Liam", "Mona", "Ned", "Olive", "Paul", "Quinn", "Rose", "Sam", "Tina",
         "Uma", "Vince", "Wendy", "Xander", "Yara", "Zack", "Amber", "Blake", "Clara", "Derek",
         "Ellen", "Felix", "Gina", "Hank", "Iris", "Jake", "Kelly", "Leo", "Maya", "Nora",
         "Oscar", "Penny", "Quincy", "Rita", "Steve", "Tara", "Ulysses", "Vera", "Walter", "Xena",
         "Yvonne", "Zane", "Anna", "Bill", "Cindy", "Doug", "Elise", "Fred", "Gloria", "Harry",
         "Isla", "John", "Katherine", "Luke", "Maggie", "Neil", "Opal", "Peter", "Queen", "Ryan",
         "Sophia", "Tom", "Ursula", "Victor", "Willow", "Ximena", "Yosef", "Zoe", "Alex", "Britney",
         "Chris", "Donna", "Eddie", "Faith", "George", "Holly", "Ian", "Julia", "Kevin", "Linda",
         "Mark", "Nate", "Olga", "Phil", "Quinton", "Rachel", "Shawn", "Tiffany", "Umar", "Valerie",
         "Wayne", "Xavier", "Yvette", "Zelda", "Aaron", "Briana", "Craig", "Dana", "Emil", "Fiona",
         "Gabe", "Hope", "Ivan", "Jill", "Karl", "Laura", "Mason", "Nina", "Owen", "Patty", "Quin",
         "Ralph", "Sally", "Tim", "Una", "Violet", "Wesley", "Xiao", "Yanni", "Zane", "Arthur", "Bella",
         "Caleb", "Diana", "Evan", "Faith", "George", "Hannah", "Isaac", "Jenna", "Kurt", "Leah", "Milo",
         "Oliver", "Paula", "Quinn", "Rob", "Sara", "Teddy", "Una", "Vera", "Will", "Xena", "Yuri",
         "Zara", "Asher", "Brielle", "Caden", "Delilah", "Eli", "Fiona", "Gideon", "Hazel", "Isaiah", "Jade",
         "Kai", "Lila", "Miles", "Nora", "Piper", "Quentin", "Ruby", "Seth", "Tara", "Uriah", "Violet",
         "Wes", "Xenia", "Yosef", "Zara", "Anna", "Ben", "Cassie", "Dylan", "Elle", "Finn", "Gina", "Hugo",
         "Levi", "Mia", "Noah", "Olivia", "Parker", "Quinn", "Riley", "Sophie", "Theo", "Umar", "Vance", "Wyatt"]

# Verify the length of the names list
if len(names) != 200:
    raise ValueError("The names list must contain exactly 200 unique names.")

# Create sample data for 200 users
data = []
for i in range(200):
    name = names[i]
    age = random.randint(18, 60)  # Random age between 18 and 60
    data.append({"Id": i + 1, "Name": name, "Age": age})

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to Excel file
df.to_excel("200_unique_users_output.xlsx", index=False)

print("Data for 200 unique users has been saved to 200_unique_users_output.xlsx")
