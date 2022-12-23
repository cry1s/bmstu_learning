#[macro_use] extern crate rocket;
macro_rules! calculator {
    ($a:expr, $b:expr, $op:expr) => {
        match $op {
            "+" => $a + $b,
            "-" => $a - $b,
            "*" => $a * $b,
            "/" => $a / $b,
            _ => 0
        }
    };
}

macro_rules! factorial {
    ($n:expr) => {
        {
            let mut result = 1;
            for i in 1..=$n {
                result *= i;
            }
            result
        }
    };
}


#[get("/hello/<name>/<age>")]
fn hello(name: &str, age: u8) -> String {
    format!("Hello, {} year old named {}!", age, name)
}

#[get("/?<a>&<b>&<op>")]
fn calc(a: i32, b: i32, op: &str) -> String {
    format!("{} {} {} = {}", a, op, b, calculator!(a, b, op))
}

#[get("/fact/<n>")]
fn fact(n: u32) -> String {
    format!("{}! = {}", n, factorial!(n))
}
#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![hello, calc, fact])
}

#[cfg(test)]
mod tests {
    use super::*;
    use rocket::local::blocking::Client;

    #[test]
    fn test_hello() {
        let client = Client::tracked(rocket()).expect("valid rocket instance");
        let response = client.get("/hello/John/20").dispatch();
        assert_eq!(response.status(), rocket::http::Status::Ok);
        assert_eq!(response.into_string(), Some("Hello, 20 year old named John!".into()));
    }

    #[test]
    fn test_calc() {
        let client = Client::tracked(rocket()).expect("valid rocket instance");
        let response = client.get("/?a=10&b=5&op=*").dispatch();
        assert_eq!(response.status(), rocket::http::Status::Ok);
        assert_eq!(response.into_string(), Some("10 * 5 = 50".into()));
    }

    #[test]
    fn test_fact() {
        let client = Client::tracked(rocket()).expect("valid rocket instance");
        let response = client.get("/fact/5").dispatch();
        assert_eq!(response.status(), rocket::http::Status::Ok);
        assert_eq!(response.into_string(), Some("5! = 120".into()));
    }
}