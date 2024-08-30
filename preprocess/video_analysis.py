import cv2
import os

vid_path = '/Users/irisnguyen/Documents/Utah PhD/Neurosymbolic Research/Code/IO/gopro/GH010069.MP4'
num_frames = 100
imgs_path = '/Users/irisnguyen/Documents/Utah PhD/Neurosymbolic Research/Code/IO/imagesOutput/NaieveSamples'

def sample_frames(vid, num_frames):
    total_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"total frames is {total_frames}")

    if num_frames > total_frames:
        num_frames = total_frames
    
    frame_indices = [int(i * total_frames / num_frames) for i in range(num_frames)]
    frames = []

    for frame_index in frame_indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    return frames

def save_imgs(folder_path, image_array):
    for i in range(len(image_array)):
        img = cv2.cvtColor(image_array[i], cv2.COLOR_RGB2BGR)

        file_name = "sample-"+str(i)+".jpg"
        file_path = os.path.join(folder_path, file_name)
        cv2.imwrite(file_path, img)

if __name__ == "__main__":
# Check if the video opened successfully
    cap = cv2.VideoCapture(vid_path)

    if not cap.isOpened():
        print("Error opening video file")

    sampled_frames = sample_frames(cap, num_frames)
    
    save_imgs(imgs_path, sampled_frames)
    # Release the video capture object
    cap.release()

    
    # for i, frame in enumerate(sampled_frames):
    #     print(type(frame))
    #     cv2.imshow(f"Frame {i}", frame)
    #     cv2.waitKey(0)
    cv2.destroyAllWindows() # Close all OpenCV windows