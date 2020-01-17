/****************************** Find queries ******************************/
// Todos as companhias que tenham relações em que o title contenha CEO
db.companies.find({
    "relationships.title": /CEO/
}, {
    "name": 1
}).pretty()

// Todas as companhias que tenha total_money_raised maior que 0
db.companies.find({
    "total_money_raised": {
        $gt: "$0"
    }
}, {
    "name": 1,
    "total_money_raised": 1
}).pretty()

// Nome da companhia mais antiga e o respetivo ano de fundação(founded_year)
db.companies.find({
    founded_year: {
        $not: {
            $type: "null"
        }
    }
}, {
    founded_year: 1,
    name: 1
}).sort({
    founded_year: 1
}).limit(1).pretty()

// Todas as empresas (nome) cujo resumo tenha menos de 30 palavras
db.companies.find({
    "overview": {
        $exists: true,
        $ne: null
    },
    $expr: {
        $lt: [{
            $size: {
                $split: ["$overview", " "]
            }
        }, 40]
    }
}, {
    name: 1
}).pretty()

// Todas as empresas (nome, url e endereço de email) que não possuam escritórios na América
db.companies.find({
    "offices.country_code": {
        $ne: "USA"
    }
}, {
    name: 1,
    homepage_url: 1,
    email_address: 1
}).pretty()

// Todas as empresas (nome) cujo código postal não possua o algarismo 0 (mas que não seja null)
db.companies.find({
    "offices.zip_code": {
        $exists: true,
        $ne: null
    },
    "offices.zip_code": {
        $not: /1/
    }
}, {
    "name": 1
}).pretty()




/****************************** Aggregate queries ******************************/
// Média de empregados
db.companies.aggregate({
    $group: {
        _id: null,
        avg_emplo: {
            $avg: "$number_of_employees"
        }
    }
})

// Top 5 dos títulos das pessoas  com mais relações
db.companies.aggregate([{
        $unwind: '$relationships'
    },
    {
        $group: {
            _id: "$relationships.title",
            sum_rel: {
                $sum: 1
            }
        }
    },
    {
        $sort: {
            sum_rel: -1
        }
    },
    {
        $limit: 5
    }
])

// Nas competitions, o competitor que competiu mais vezes
db.companies.aggregate([{
        $unwind: "$competitions"
    },
    {
        $group: {
            _id: "$competitions.competitor",
            sum_c: {
                $sum: 1
            }
        }
    },
    {
        $sort: {
            sum_c: -1
        }
    },
    {
        $limit: 1
    }
])

// Quantas empresas têm offices na Russia
db.companies.aggregate([{
        $unwind: "$offices"
    },
    {
        $group: {
            _id: "$offices.country_code",
            sum_c: {
                $sum: 1
            }
        }
    },
    {
        $match: {
            _id: {
                $eq: "RUS"
            }
        }
    }
])

// O tamanho do maior resumo
db.companies.aggregate([{
    $match: {
        "overview": {
            $nin: ["", null]
        }
    }
}, {
    $project: {
        length: {
            $strLenCP: "$overview"
        },
        name: 1
    }
}, {
    $group: {
        _id: null,
        max_length: {
            $max: "$length"
        }
    }
}])

// Quantos estados diferentes onde estão localizados os escritórios há
db.companies.aggregate([{
    $unwind: "$offices"
}, {
    $match: {
        "offices.state_code": {
            $nin: ["", null]
        }
    }
}, {
    $group: {
        _id: null,
        state: {
            $addToSet: "$offices.state_code"
        }
    }
}, {
    $unwind: "$state"
}, {
    $group: {
        _id: null,
        count: {
            $sum: 1
        }
    }
}]).pretty()

// Empressa que tem mais escritórios
db.companies.aggregate([{
    $project: {
        num_offices: {
            $size: "$offices"
        },
        name: 1
    }
}, {
    $sort: {
        num_offices: -1
    }
}, {
    $limit: 1
}])

// Média do ano de fundação
db.companies.aggregate([{
    $group: {
        _id: null,
        avg: {
            $avg: "$founded_year"
        }
    }
}])