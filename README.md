# Sinyaller ve Sistemler - Ödev 1: İşaret Analizi ve DTMF Sentezi

Bu proje, İstanbul Sağlık ve Teknoloji Üniversitesi (İSTÜN) Bilgisayar Mühendisliği bölümü **Sinyaller ve Sistemler** dersi kapsamında hazırlanan birinci ödev çalışmasıdır. Proje, analog işaretlerin dijital ortamda örneklenmesi, Nyquist teoremi ve DTMF (Çift Tonlu Çoklu Frekans) sinyallerinin sentezlenmesini konu almaktadır.

## 👥 Grup Üyeleri
* **Meryem Sena Umutlu** - 240601066
* **Zeynep Umutlu** - 240601010
* **Rümeysa Yapar** - 230601059

---

## 🚀 Proje Görevleri

### 1. Sinüzoidal İşaret Analizi (Görev 1)
Bu bölümde belirlenen $f_0 = 135$ Hz temel frekansı kullanılarak aşağıdaki işaretler üretilmiştir:
* $f_1 = f_0$ (135 Hz)
* $f_2 = f_0 / 2$ (67.5 Hz)
* $f_3 = 10 \cdot f_0$ (1350 Hz)

**Nyquist Gerekçelendirmesi:** Sinyallerin bozulmadan (aliasing oluşmadan) temsil edilmesi için örnekleme frekansı ($f_s$), sinyaldeki en yüksek frekansın ($f_3 = 1350$ Hz) en az iki katı olmalıdır. Projede, hem görsel sürekliliği sağlamak hem de standart ses kalitesine uyum sağlamak amacıyla $f_s = 44100$ Hz seçilmiştir.

### 2. DTMF Sinyal Sentezi ve Arayüzü (Görev 2)
Telefon tuş takımı seslerini üreten interaktif bir Python uygulamasıdır.
* **Arayüz:** Tkinter kullanılarak 0-9, A-D, *, # tuşlarını içeren bir numpad tasarlanmıştır.
* **Sentez:** Her tuşa basıldığında, o tuşa özgü düşük ve yüksek frekans gruplarından iki sinüs dalgası toplanarak ($x(t) = \sin(2\pi f_{low}t) + \sin(2\pi f_{high}t)$) çalınmaktadır.
* **Görselleştirme:** Üretilen sinyal anlık olarak zaman domaininde grafiklenmektedir.

---

## 🛠️ Kurulum ve Çalıştırma

Projenin çalışması için sisteminizde Python yüklü olmalıdır. Gerekli kütüphaneleri yüklemek için:

```bash
pip install numpy matplotlib sounddevice
