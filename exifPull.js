const imgElement = document.getElementById('gallery-photo');

imgElement.onload = function() {
    EXIF.getData(imgElement, function() {
        const allMetaData = EXIF.getAllTags(this);
        
        // Map EXIF tags to your UI
        const dataMap = {
            'Model': allMetaData.Model,
            'Lens': allMetaData.LensModel,
            'ISO': allMetaData.ISOSpeedRatings,
            'F-Stop': `f/${allMetaData.FNumber}`,
            'Shutter': `${allMetaData.ExposureTime}s`,
            'Focal Length': `${allMetaData.FocalLength}mm`
        };

        // Update the DOM
        Object.keys(dataMap).forEach(key => {
            const el = document.querySelector(`[data-exif="${key}"]`);
            if (el) el.innerText = dataMap[key] || 'N/A';
        });
    });
};