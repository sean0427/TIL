package proxy;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;
import java.util.Date;

class ProxyPractice {
    Subject proxyClass;

    ProxyPractice() {
        proxyClass = (Subject) Proxy.newProxyInstance(
                ProxyPractice.class.getClassLoader(),
                RealSubject.class.getInterfaces(),
                new Proxys(new RealSubject()));
    }

    public void run() {
        proxyClass.request();
    }

    public void runAA() {
        System.out.println(proxyClass.requestAA());
    }

    public static void main(String[] args) {
        ProxyPractice p = new ProxyPractice();
        p.run();
        p.runAA();
    }

}

interface Subject {
    public void request();
    public String requestAA();
}

class RealSubject implements Subject {
    public void request() {
        System.out.println("request");
    };

    public String requestAA() {
        return "AA";
    };
}

class Proxys implements InvocationHandler {
    private final Subject subject;

    public Proxys(Subject subject) {
        this.subject = subject;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        System.out.println(method.getName() + "start: " + new Date());

        Object result = method.invoke(subject, args);

        System.out.println(method.getName() + "end:" + new Date());

        if (result instanceof String) {
            return "Proxy " + ((String) result).toUpperCase();
        }
        return result;
    }
}