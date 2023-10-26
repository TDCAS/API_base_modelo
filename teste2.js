// Dados da solicitação POST
const apiUrl = 'http://127.0.0.1:5000/query'; // A mesma URL usada no comando curl
const contentType = 'application/sql'; // Tipo de conteúdo apropriado para a sua API
const sqlQuery = 'SELECT * FROM Clientes'; // Sua consulta SQL

// Cabeçalhos da solicitação
const headers = {
    'X-API-KEY': 'Messem@2023', // Adicione o cabeçalho X-API-KEY
    'Content-Type': contentType,
};

// Corpo da solicitação
const data = sqlQuery;

// Enviando a solicitação POST
fetch(apiUrl, {
  method: 'POST',
  headers: headers,
  body: data,
})
  .then(response => {
    // Verifique se a resposta da API é bem-sucedida (código de status 200)
    if (response.status === 200) {
      return response.json(); // Converte a resposta para JSON
    } else {
      throw new Error('Falha na solicitação POST');
    }
  })
  .then(apiResponse => {
    console.log('Solicitação POST bem-sucedida');
    console.log('Resposta da API:', apiResponse);
  })
  .catch(error => {
    console.error(error); // Lida com erros, se houver algum
  });
