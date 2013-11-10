#include <iostream>

class OnlineStat {
public:
  OnlineStat() {
    mean = 0;
    sq_avg = 0;
    variance = 0;
    num_samples = 0;
  }
  ~OnlineStat() {}
  
  void add_sample(float x) {
    // Update mean
    mean = (num_samples * mean + x) / (num_samples + 1);
    sq_avg = (num_samples * sq_avg + x*x) / (num_samples + 1);
    // Update variance    
    variance = sq_avg - mean*mean; 
    num_samples += 1;
  }
  
  float get_variance() {
    return variance;
  }

  float get_mean() {
    return mean;
  }
private:  
  float mean;
  float sq_avg; 
  float variance;
  int num_samples;

};

int main() {
  OnlineStat os;
  float samples[] = {4.2, 4.5, 1.2, -3.4, 3.6, 1.2, 5.6, -4.2, 3.6};
  int num_samples = 9;
  float mean = 0;
  float sq_avg = 0;
  float variance = 0;

  for (int i = 0; i < num_samples; i++) {
    mean += samples[i];
    sq_avg += samples[i] * samples[i];
    os.add_sample( samples[i] );
  }
  mean /= num_samples;
  sq_avg /= num_samples;
  variance = sq_avg - mean*mean;
  
  std::cout << "Offline mean: " << mean << std::endl << "Offline variance: " << variance << std::endl;
  std::cout << "Online mean: " << os.get_mean() << std::endl << "Online variance: " << os.get_variance() << std::endl;
  
  return 0;
}
