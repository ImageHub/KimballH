import os
import json

# 1. Go directly to script.google.com.
# 2. Run the Get fileIDs script (it should already be there but here it is anyway)
# function listFolderContents() {
#   // 1. GET THE FOLDER ID
#     // open the folder on the Google Drive Web Interface. 
#     // Look at your browser's address bar
#     // copy the long, random string of letters and numbers that comes immediately after /folders/.
#     // 1iimta3YBZ3pRaYiB45BMQspg9EzkgHdX
#     // put it in quotes and set folderID = to it
#     // click save, then run
#     
#   var folderId = '1iimta3YBZ3pRaYiB45BMQspg9EzkgHdX'; 
#   
#   var folder = DriveApp.getFolderById(folderId);
#   var files = folder.getFiles();
#   var output = {};
#   
#   while (files.hasNext()) {
#     var file = files.next();
#     // Maps the file basename (without extension) to its Google Drive ID
#     var nameWithoutExt = file.getName().replace(/\.[^/.]+$/, "");
#     output[nameWithoutExt] = file.getId();
#   }
#   
#   Logger.log(JSON.stringify(output, null, 2));
# }
# 
# // look in the execution log fileIDs script and copy the entire block of IDs
# 3. PASTE THE ENTIRE OBJECT YOU COPIED FROM GOOGLE APPS SCRIPT LOGS HERE:
DRIVE_MAP = {
   "Boxster": "1AnMnZnqKM6zhqAdFC2uFUTj06krSnSAg",
  "B0000154": "1MLkPJDzkNCDXakRabiqyeyDPDU9UaHPL",
  "B0000153": "1lgqCagRlvtn8cdVJxrNVbAsrWxGTESeK",
  "B0000151": "1-OapeChI4Us8p1i-4dYgip7UH95Ycv1t",
  "B0000150": "1m6H2eCW3QfM7X2BphH5-FOE6FPTKl2pE",
  "B0000147": "1-bzosrFFH1pg-0qBtxneO8ktLShilNeK",
  "B0000146": "1kSVw6NzU8qUkpvgHNd5I-uNgTul8_cWV",
  "B0000145": "1DHYfS1drjasJ5YV5zWdn8kwh5WLs6ail",
  "B0000144": "1IDmRMvPerqR66yDYopjhn9-STvCb4Hqb",
  "B0000141": "1FGYm_gKtXNzif2SBD2Eue7ISwmRYTAvp",
  "B0000140": "1UmofT_2Z4AdQInDbJ9B72lCfAlYaRmsL",
  "B0000139": "1LpUZUwrnYmvHErW46NrE2cD83ot1VqOF",
  "B0000137": "14YyLhXsAFdzu5Kzr9QDnCiBw92I2yx6j",
  "B0000135": "1h211xyg8q2vjibYSWd-dpzOl2mzOQMel",
  "B0000134": "1uLm80v8LYMvqwYkynd-CWhqpqL438nJs",
  "B0000133": "1q1Ug7os4F0O5DJ-GaWnTf32cBwU-m4-L",
  "B0000132": "12haQBWjq0tKeUuk2PENXE4f-zqu7G6nY",
  "B0000131": "12Uzs4tmKriN3aVwyWESKmZW80QH5SkR4",
  "B0000130": "1yDQbymUkgI4Ka57Drljq2kwlbDmTZkED",
  "B0000128": "1YDFeULLj9fPddhyDCLa00XZwRHtfvk1R",
  "B0000127": "1aspq6F4cowiMkpDPdvxkbsMcrRZwi4I-",
  "B0000121": "1EG5F26pDLtT_bUXZ-Nw2mK4KqY4fb7w6",
  "B0000120": "1rn9ZMGbGBL1OQUY4qISU6i12dkzhrVEk",
  "B0000117": "1SZIMlQidBrabG7lVEM4vMdzxzBfNQmJu",
  "B0000115": "1Oqky6mm9vPX3yMyheLzpsVHgIHWgpGqg",
  "B0000113": "17c8CuQBNFxJiiydmhKPfcbwCKfoAPh8o",
  "B0000111": "1LRSpg3RChXi98AwejZDC8Sb8hXRTBcPj",
  "B0000109": "1KjViS0mP_YKIchrIidzz7cs2yq_6HGNt",
  "B0000108": "1IXwwV_aJGHr3fvmAya0ZYwU5qw9TS9Or",
  "B0000107": "19PMIw-4GiwXwdsAI-MF2s0_2l-tp9B1O",
  "B0000105": "169PN35SAZct_tLr9qFPXTLCKX1bS2VZM",
  "B0000104": "1q7hOO-8VoF7fnFXvPvlTXDGyLZvRmyVk",
  "B0000100": "1vWq6JmZLi7LGpx3nIirLqnglqLdasFk3",
  "B0000099": "1hDBGOK31rl2WHvPjyW6wvWYpOnaqPrWO",
  "B0000097": "1X31jXddpf8H45uzj77wQEHsH9h0yC715",
  "B0000095": "1DWVWLyiKosUgNfS1_K1SFUq2xQK35g9U"

}


JSON_PATH = "gallery-data.json"

def main():
    if not os.path.exists(JSON_PATH):
        print(f"Error: {JSON_PATH} not found.")
        return

    with open(JSON_PATH, 'r') as f:
        gallery_data = json.load(f)

    updated_count = 0
    missing_count = 0

    for entry in gallery_data:
        source = entry.get("SourceFile", "")
        # Get just the file name (e.g., "B0000095.heif" or "B0000095.avif")
        filename = os.path.basename(source)
        # Get just the base name without extension ("B0000095")
        base_name, _ = os.path.splitext(filename)

        if base_name in DRIVE_MAP:
            file_id = DRIVE_MAP[base_name]
            entry["SourceFile"] = f"https://lh3.googleusercontent.com/d/{file_id}"
            updated_count += 1
        else:
            missing_count += 1

    with open(JSON_PATH, 'w') as f:
        json.dump(gallery_data, f, indent=2)

    print(f"Successfully mapped {updated_count} files to Google Drive direct links!")
    if missing_count > 0:
        print(f"Could not find matching Drive IDs for {missing_count} entries in your JSON.")

if __name__ == "__main__":
    main()