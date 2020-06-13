import json, hashlib, sys, subprocess, os
from external import CCourse
from external import CPerson


people = []

def hashExists(hashcode):
    index = 0;
    for person in people:
        if person.Hashcode == hashcode:
            return index;
        index += 1
    return - 1

def convertToDate(stringDateFrom, stringDateTo):
    year = stringDateFrom[0:4]
    month = stringDateFrom[5:7]
    day = stringDateFrom[8:10]
    hourFrom = stringDateFrom[11:13]
    minuteFrom = stringDateFrom[14:16]
    hourTo = stringDateTo[11:13]
    minuteTo = stringDateTo[14:16]

    numeric = int(minuteFrom) + 60 * int(hourFrom) + 24 * int(day) + 31 * int(month)

    output = "{0}.{1}.{2} {3}:{4} - {5}:{6}".format(day, month, year, hourFrom, minuteFrom, hourTo, minuteTo)
    return {'string':output, 'integer':numeric};

def loadInfo(path):
    try:
        f = open(path, encoding="utf8")
        d = json.load(f)

        for element in d:
            if element['Buchung Status'] == 'Angenommen':
                prename = element['Teilnehmer Vorname']
                lastname = element['Teilnehmer Nachname']
                email = element['Benutzer Login']          # for exact definition of person

                coursname = element['Angebot Titel']

                coursdateFrom = element['Durchführung Daten'][0][0]
                coursdateTo = element['Durchführung Daten'][0][1]
                coursedate = convertToDate(coursdateFrom, coursdateTo)

                hashcode = hash(prename + lastname + email)

                course = CCourse(coursname, coursedate['string'], coursedate['integer'])

                personIndex = hashExists(hashcode)

                if (personIndex < 0):
                    person = CPerson(hashcode, prename, lastname, course);
                    people.append(person)
                else:
                    people[personIndex].addCourse(course)
        print(str(len(people)) + " Personen gefunden.")
    except:
        print("Die Datei konnte nicht geöffnet werden.")
        input()
        sys.exit(0)


def sortPeople():
    for person in people:
        person.sortByDate()

def createFile(path):
    Text = "Vorname;Nachname;Datum1;Kurs1;Datum2;Kurs2;Datum3;Kurs3;Datum4;Kurs4;Datum5;Kurs5;Datum6;Kurs6;Datum7;Kurs7;Datum8;Kurs8;Datum9;Kurs9;Datum10;Kurs10;Datum11;Kurs11;Datum12;Kurs12;Datum13;Kurs13;Datum14;Kurs14;Datum15;Kurs15;Datum16;Kurs16;Datum17;Kurs17;Datum18;Kurs18;Datum19;Kurs19;Datum20;Kurs20;Datum21;Kurs21;Datum22;Kurs22;Datum23;Kurs23;Datum24;Kurs24;Datum25;Kurs25\n"
    for person in people:
        Text += person.Prename + ";" + person.Lastname

        for i in range(0, 25):
            if i < len(person.Courses):
                Text += (";" + person.Courses[i].Date + ";" + person.Courses[i].Name)
            else:
                Text += (";;")
        Text = "{0}\n".format(Text)
    print("Daten Konvertiert.")

    try:
        f = open(path, "w", encoding="utf8")
        f.write(Text)
        f.close()
        print("Die Datei wurde gespeichert.")
        dir = os.getcwd() + '\\' + path
        print(dir)
        subprocess.Popen(r'explorer /select,"' + dir + '"')
    except:
        print("Die Datei konnte nicht gespeichert werden.")
        input()
        sys.exit(0)



# Main Programm
print("\n============================================================\nFerienspass converter      (c)Alexander Romberg\n============================================================\n\nDie geforderte JSON-Datei lässt sich von https://stein-am-rhein.feriennet.projuventute.ch herunterladen oder kopieren.\nHierfür bitte nach der Anmeldung auf \"Ferienspass 20**\" > \"Exporte\" > \"Wunschliste / Buchungen\" > \"JSON Datei\" > \"Absenden\" wählen\n\n")
path = input('Bitte die JSON-Datei von Feriennet hier hin ziehen und {ENTER} drücken: ')
loadInfo(path)
sortPeople()
createFile('KonvertierteDaten.csv')
print("Fertig!")
input("Das Fenster kann jetzt geschlossen werden")
