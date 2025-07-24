const http = require('http');

function cpuIntensiveTask(ms) {
  const end = Date.now() + ms;
  while (Date.now() < end); // Block the event loop
}

const server = http.createServer((req, res) => {
  // Log basic request info
  const now = new Date().toISOString();
  const ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
  console.log(`[${now}] ${req.method} ${req.url} from ${ip}`);

  // Burn CPU
  cpuIntensiveTask(300);

  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Heavy CPU task done!\n');
});

server.listen(8080, () => {
  console.log('Server running on http://localhost:8080');
});
