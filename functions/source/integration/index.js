var http = require('http');
var path = require('path');
var integrationEndpoint = process.env['IntegrationEndpoint'];

exports.handler = function (event, context) {
    console.log('Getting pet type cat')
    http.get(path.join(integrationEndpoint, '2'), function (result) {
        console.log('Success, with: ' + result.statusCode);
        context.done(null);
    }).on('error', function (err) {
        console.log('Error, with: ' + err.message);
        context.done("Failed");
    });
};
