import org.junit.Before;
import org.junit.Ignore;
import org.junit.Test;

import java.io.Console;
import java.util.Locale;
import java.util.concurrent.TimeUnit;

import io.reactivex.Observable;
import io.reactivex.ObservableEmitter;
import io.reactivex.ObservableOnSubscribe;
import io.reactivex.Scheduler;
import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Action;
import io.reactivex.functions.Consumer;

import static org.junit.Assert.*;
/**
 * Learn for RxJava
 * Created by sean on 2017/9/6.
 */

public class RxJavaTest {

    private static int I = 1;

    interface IFace {
        default String doSomeThing() {
            return this.getClass().getSimpleName();
        }
    }

    class Klass implements IFace {

    }

    class Klass1 implements IFace {
    }

    @Before
    public void setup() {
    }

    @Test
    public void test() {
        Observable<Integer> observable = Observable.create(new ObservableOnSubscribe<Integer>() {
            @Override
            public void subscribe(ObservableEmitter<Integer> e) throws Exception {
                e.onNext(1);
            }
        }).startWithArray(1,2,3);

        observable.subscribe(System.out::println);
    }

    @Test
    public void Query() {
        Observable<Integer> observable = Observable.just(1,2,2,2);
    }

    @Test
    public void JustCreateAndMap() {
        Observable<Integer> observable = Observable.just(1,2,2,2);
        observable.map((i) -> i+100) .subscribe(System.out::println);
    }

    @Test
    public void SubscribeByConsumer() {
        Consumer<IFace> onNext = (iface) -> {
            assertEquals(iface.getClass().getSimpleName(), iface.doSomeThing());
            System.out.println(String.format(Locale.getDefault(),"%s\t%d",iface.doSomeThing(), I++));
        };
        Consumer<Throwable> onError = Throwable::printStackTrace;
        Action onComplete = () -> System.out.println("complete!");

        Observable<IFace> observable = Observable.fromArray(new Klass(), new Klass1())
                .doAfterNext(iFace -> System.out.println(iFace.toString()));

        observable.subscribe(onNext, onError, onComplete);


        /*
         if thread is stop, it will not be called.
         try {
             Thread.sleep(10000);
         } catch (InterruptedException e) {
             e.printStackTrace();
         }
        */
        observable.delay(10, TimeUnit.SECONDS).subscribe(onNext).dispose();

        final IFace iFace = new IFace() {
            @Override
            public String doSomeThing() {
                return "inner";
            }
        };

    }
}
