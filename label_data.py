import pandas as pd
import re

def assign_genre(lyric):
    if pd.isna(lyric):
        return "อื่นๆ"
        
    lyric_str = str(lyric)
    
    # Define keywords for each genre
    love_keywords = ["รัก", "คิดถึง", "กอด", "จูบ", "แฟน", "หัวใจของเรา", "ที่รัก", "แอบชอบ", "ใจสั่น", "โรแมนติก", "หวาน", "อินเลิฟ", "ความสุข", "ห่วงใย", "ดูแล"]
    sad_keywords = ["เศร้า", "อกหัก", "น้ำตา", "เจ็บ", "ทิ้ง", "ลืม", "ร้องไห้", "เหงา", "ปวดร้าว", "จากลา", "เดียวดาย", "ทรมาน", "พัง", "เสียใจ", "บอกลา", "เลิก", "รอยแผล"]
    folk_keywords = ["อีสาน", "ทุ่งนา", "พิณ", "แคน", "หมอลำ", "ลูกทุ่ง", "บ้านนา", "บ่าว", "สาว", "เซิ้ง", "ภูธร", "ควาย", "ฮัก", "อ้าย", "น้องนาง", "เด้อ", "เว่า", "ซิ่น", "สะล้อ", "ซอ", "ซึง", "ล้านนา", "ปักษ์ใต้", "โนราห์", "หนังตะลุง", "แหล่"]
    thai_inter_keywords = ["ชิล", "ปาร์ตี้", "เพื่อน", "จังหวะ", "ดนตรี", "เต้น", "สนุก", "แร็พ", "สแวก", "ร็อค", "ฝัน", "ชีวิต", "สู้", "หวัง", "วัยรุ่น", "สไตล์", "บีท", "ฮิปฮอป", "อิสระ", "เดินทาง", "ก้าว", "วันใหม่"]
    
    # Count occurrences
    love_score = sum(1 for kw in love_keywords if kw in lyric_str)
    sad_score = sum(1 for kw in sad_keywords if kw in lyric_str)
    folk_score = sum(1 for kw in folk_keywords if kw in lyric_str)
    thai_inter_score = sum(1 for kw in thai_inter_keywords if kw in lyric_str)
    
    # Determine max score
    scores = {
        "เพลงเศร้า": sad_score,
        "เพลงรัก": love_score,
        "เพลงพื้นบ้าน": folk_score,
        "เพลงไทยสากล": thai_inter_score
    }
    
    max_score = max(scores.values())
    
    if max_score == 0:
        return "อื่นๆ"
        
    # Get the genre(s) with the max score
    top_genres = [genre for genre, score in scores.items() if score == max_score]
    
    # Tie-breaking logic (priority: Sad > Folk > Love > Thai Inter)
    if "เพลงเศร้า" in top_genres:
        return "เพลงเศร้า"
    elif "เพลงพื้นบ้าน" in top_genres:
        return "เพลงพื้นบ้าน"
    elif "เพลงรัก" in top_genres:
        return "เพลงรัก"
    elif "เพลงไทยสากล" in top_genres:
        return "เพลงไทยสากล"
        
    return "อื่นๆ"

def main():
    print("Loading output_file.csv...")
    try:
        df = pd.read_csv('d:/Users/erk/Desktop/thai_song_nlp-main/thai_song_nlp-main/output_file.csv')
    except Exception as e:
        print(f"Error reading file: {e}")
        return
        
    print(f"Total songs loaded: {len(df)}")
    
    print("Assigning genres based on lyrics keywords...")
    df['label'] = df['lyric'].apply(assign_genre)
    
    print("\nGenre Distribution:")
    print(df['label'].value_counts())
    
    output_path = r'd:\Users\erk\Desktop\thai_song_nlp-main\thai_song_nlp-main\labeled_songs.csv'
    df.to_csv(output_path, index=False)
    print(f"\nSaved labeled dataset to: {output_path}")

if __name__ == "__main__":
    main()
