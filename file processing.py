# Exercise 1

with open("input.txt", "r") as file1:
		file_data= file1.read()
		
print(file_data)



# Exercise 2
with open("online reviews.txt", "r") as file_online_reviews:
        for line in file_online_reviews.readlines():
            if "horrible" in line.split(' - ')[3].lower():
                    print(line.split(' - ')[0])


# Exercise 3
count_5_stars = 0
with open("online reviews.txt", "r") as file_online_reviews:
        for line in file_online_reviews.readlines():
            if "5 stars" in line.split(' - ')[2]:
                    count_5_stars += 1
print(count_5_stars)


# Exercise 3V2
count_5_starsV2 = sum(1 for line in open("online reviews.txt", 'r') if "5 stars" in line.split(' - ')[2])
print(count_5_starsV2)



# Exercise Tabular
with open("events.tsv", "r") as registry_tabular:
        
        registry_list = []
        registrykeys = ["show", "event", "timestamp", "user_id"]
        for line in registry_tabular.readlines():
                line = line.strip().split("\t")
                registry = {}
                for i in range(len(registrykeys)):
                        registry[registrykeys[i]] = line[i]
                registry_list.append(registry)
        #print(registry_list)


def conver_tabular_file_content_to_dictionary(filename) -> dict:
        with open(filename, "r") as registry_tabular:
                registry_list = []
                registrykeys = ["show", "event", "timestamp", "user_id"]
                for line in registry_tabular.readlines():
                        line = line.strip().split("\t")
                        registry = {}
                        for i in range(len(registrykeys)):
                                registry[registrykeys[i]] = line[i]
                        registry_list.append(registry)
                return(registry_list)
        

print(conver_tabular_file_content_to_dictionary(("events.tsv")))
        








