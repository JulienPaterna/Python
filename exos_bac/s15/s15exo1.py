t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 12.4]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

def mini(releve, date):
    t_mini = releve[0]
    annee = date[0]
    for i in range(1, len(releve)):
        if (releve[i] < t_mini):
            t_mini = releve[i]
            annee = date[i]
    return t_mini, annee



print(mini(t_moy, annees))