#include <iostream>

class Strategy {
public:
  Strategy() {}
  ~Strategy() {}
  virtual void behavior() {}
};

class ConcreteStrategyA : public Strategy {
  void behavior () {
    std::cout << "ConcreteStrategyA" << std::endl;
  }
};

class ConcreteStrategyB : public Strategy {
  void behavior () {
    std::cout << "ConcreteStrategyB" << std::endl;
  }
};

class ConcreteStrategyC : public Strategy {
  void behavior () {
    std::cout << "ConcreteStrategyC" << std::endl;
  }
};

class Context {
public:
  Context(Strategy *strategy_) {
    strategy = strategy_;
  }
  ~Context() {
    delete strategy;
  }
  void method() {
    strategy->behavior();
  }
private:
  Strategy *strategy;
};

int main() {
  Strategy *strategy = new ConcreteStrategyB();
  Context *context = new Context(strategy);
  context->method();
  
  delete context;
  return 0;
}
