# ================================
# Run all models and save outputs
# ================================

Write-Host "Running ResNet..."
python check_images.py --dir pet_images/ --arch resnet --dogfile dog_names.txt > resnet_pet-images.txt

Write-Host "Running AlexNet..."
python check_images.py --dir pet_images/ --arch alexnet --dogfile dog_names.txt > alexnet_pet-images.txt

Write-Host "Running VGG..."
python check_images.py --dir pet_images/ --arch vgg --dogfile dog_names.txt > vgg_pet-images.txt

Write-Host ""
Write-Host "==============================="
Write-Host "Batch Processing Completed!"
Write-Host "==============================="
Write-Host ""

# ================================
# Print Results Table
# ================================

# List of output files
$files = @("resnet_pet-images.txt","alexnet_pet-images.txt","vgg_pet-images.txt")

# Initialize arrays
$models = @()
$dogsCorrect = @()
$nonDogsCorrect = @()
$breedCorrect = @()
$matchCorrect = @()
$totalImages = 0
$dogImages = 0
$nonDogImages = 0

foreach ($f in $files) {
    $content = Get-Content $f

    # Extract values
    $totalImages = ($content | Select-String "Number of Images").Line.Split(":")[1].Trim()
    $dogImages = ($content | Select-String "Correct Dogs").Line.Split(":")[1].Trim()
    $nonDogImages = ($content | Select-String "Correct NON-Dogs").Line.Split(":")[1].Trim()
    
    $dogsCorrect += $dogImages
    $nonDogsCorrect += $nonDogImages
    $breedCorrect += ($content | Select-String "Correct Breed").Line.Split(":")[1].Trim()
    $matchCorrect += ($content | Select-String "Correct Matches").Line.Split(":")[1].Trim()

    $models += ($f -replace "_pet-images.txt","")
}

# Print table
Write-Host "Results Table"
Write-Host ""
Write-Host "Total Images: $totalImages"
Write-Host "Dog Images: $dogImages"
Write-Host "Not-a-Dog Images: $nonDogImages"
Write-Host ""
Write-Host "CNN Model Architecture: " ($models -join " | ")
Write-Host "% Not-a-Dog Correct: " ($nonDogsCorrect -join " | ")
Write-Host "% Dogs Correct: " ($dogsCorrect -join " | ")
Write-Host "% Breeds Correct: " ($breedCorrect -join " | ")
Write-Host "% Match Labels: " ($matchCorrect -join " | ")

Read-Host "Press Enter to exit..."
