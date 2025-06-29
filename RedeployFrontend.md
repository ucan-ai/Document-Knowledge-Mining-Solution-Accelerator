# 1. Navigate to deployment directory
cd Deployment

# 2. Rebuild Docker image with your changes
docker build "../App/frontend-app/." --no-cache -t crkmgsqc6izqzzc4.azurecr.io/kmgs/frontapp

# 3. Push updated image to ACR
docker push crkmgsqc6izqzzc4.azurecr.io/kmgs/frontapp

# 4. Restart deployment to pull new image
kubectl rollout restart deployment/frontapp-deployment -n ns-km

# 5. Wait for completion
kubectl rollout status deployment/frontapp-deployment -n ns-km