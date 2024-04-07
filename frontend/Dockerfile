# Use the official Node.js image as the base image
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the source code to the container
COPY . .

# Build the frontend application
RUN npm run build

# Expose port 3000
EXPOSE 3000

# Command to run the frontend server
CMD ["npm", "start"]
