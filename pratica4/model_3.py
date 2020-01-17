import csv

def write_csv(file_name, data):
   with open(file_name, 'w') as file:
      writer = csv.writer(file, delimiter=',')
      writer.writerows(data)


def main():
   with open("git_selection.csv", 'r', encoding = "ISO-8859-1") as file:
      data = csv.DictReader(file)


      person = [['svn_id', 'real_name']]
      project = [['project_name', 'organization']]
      relation = [['num', 'svn_id', 'role_on_project', 'project_name']]
      for r in data:
         project.append([r['project_name'], r['organization']])
         person.append([r['svn_id'], r['real_name']])
         relation.append([r['num'], r['svn_id'], r['role_on_project'], r['project_name']])


   write_csv('git_projects.csv', project)
   write_csv('git_persons.csv', person)
   write_csv('git_relations.csv', relation)
   print("DONE")


if __name__ == "__main__":
   main()
