// Creating a pre-built image with a unique name based on the current timestamp
const imageName = `church-locations-image:${Date.now()}`;

try {
    // Create the image using the daytona library
    await daytona.createImage(imageName, imageData, { 
        onLogs: (log) => console.log(log) 
    });
    console.log(`Image "${imageName}" created successfully.`);

    // Use the pre-built image to create a sandbox environment
    const sandbox = await daytona.create({
        image: imageName,
    });
    console.log(`Sandbox created using image "${imageName}".`);
} catch (error) {
    console.error('Failed to create image or sandbox:', error);
}
