# Lightweight Node.js base
FROM node:20-alpine

# Set working dir
WORKDIR /app

# Copy source
COPY server.js .

# Expose port
EXPOSE 8080

# Start server
CMD ["node", "server.js"]
