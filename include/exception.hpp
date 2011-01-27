#include <string>

namespace Iliad {

class Exception {

public:
	virtual ~Exception(){

	}

	virtual std::string what() = 0;

protected:

	Exception(){
	
	}


};

}

