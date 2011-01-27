#include <iostream>

#include <response.hpp>

namespace Iliad {
namespace CGI {

class Response : public Iliad::Response {

public:

	Response(std::ostream& out) : Iliad::Response(){

	}

};


}
}

