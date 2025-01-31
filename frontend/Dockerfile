# Frontend Dockerfile (frontend/Dockerfile)

# ---- Build Frontend ----
    FROM node:18 AS frontend-builder

    WORKDIR /app/frontend
    
    # Copy package.json and install dependencies
    COPY frontend/package.json ./
    RUN npm install --legacy-peer-deps
    
    # Copy the rest of the frontend source code
    COPY frontend/ .
    
    # Build the frontend (e.g., React, Vue)
    RUN npm run build
    
    # ---- Serve Frontend ----
    FROM node:18 AS frontend
    
    WORKDIR /app
    
    # Copy the build files from the frontend-builder stage
    COPY --from=frontend-builder /app/frontend/build /app/frontend_build
    
    # Install serve globally to serve the static files
    RUN npm install -g serve
    
    EXPOSE 3000
    
    # Command to serve the built frontend
    CMD ["serve", "-s", "/app/frontend_build", "-l", "3000"]
    