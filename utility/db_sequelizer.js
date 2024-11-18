const Sequelize = require("sequelize");

const sequelize = new Sequelize(
    'ND_WSC',
    'sa',
    'Nde962005',
    {
        host: '127.0.0.1',
        dialect: 'mssql'
    }
);

sequelize.authenticate(id=70).then(() => {
    console.log('Connection has been established successfully.');
    sequelize.query(
        'SELECT * FROM ND_WSC WHERE ID='+id
    ).then(result => {
        console.log(result);
    }).catch((error) => {
        console.error('Failed to insert data : ', error);
    });

}).catch((error) => {
    console.error('Unable to connect to the database: ', error);
});


sequelize.authenticate(query).then(() => {
    console.log('Connection has been established successfully.');
    sequelize.query(
        'SELECT * FROM ND_WSC WHERE ID=' + id
    ).then(result => {
        console.log(result);
    }).catch((error) => {
        console.error('Failed to insert data : ', error);
    });

}).catch((error) => {
    console.error('Unable to connect to the database: ', error);
});





// sequelize
//     .query('CALL login (:email, :pwd, :device)',
//         { replacements: { email: "me@jsbot.io", pwd: 'pwd', device: 'android', } })
//     .then(v => console.log(v));
