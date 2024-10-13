FROM node:14-alpine

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package*.json ./
RUN npm install --production

# Bundle app source 
COPY . .
# Expose port
EXPOSE 8080

# Start the application 
CMD ["node", "app.js"]
