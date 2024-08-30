import cv2

vid_path = '/Users/irisnguyen/Documents/Utah PhD/Neurosymbolic Research/Code/input/gopro/GH010069.MP4'
num_frames = 10


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

if __name__ == "__main__":
# Check if the video opened successfully
    cap = cv2.VideoCapture(vid_path)

    if not cap.isOpened():
        print("Error opening video file")

    sampled_frames = sample_frames(cap, num_frames)
    
    # Release the video capture object
    cap.release()

    
    for i, frame in enumerate(sampled_frames):
        cv2.imshow(f"Frame {i}", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows() # Close all OpenCV windows