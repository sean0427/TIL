
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.annotations.SerializedName;

import org.junit.Test;

import java.util.Locale;

import static org.junit.Assert.*;
/**
 * Practice for GSon.
 * Created by sean on 2017/9/11.
 */
public class GSonTest {
    private class Klass {
        @SerializedName("TEXT")
        public String text = "a";

        @SerializedName("integer")
        public int anInt = 1;

        @Override
        public String toString() {
            return String.format(Locale.getDefault(),
                    "TEXT: %s, integer: %d",
                    text, anInt
            );
        }
    }

    private static final String TEXT = "test";
    private static final int NUMBER = 0;

    private static final String JSON_TEXT = String.format(
            Locale.getDefault(),
            "{\"TEXT\": %s, \"integer\": %d}",
            TEXT, NUMBER
    );

    @Test
    public void unserialize() {
        Gson gson = new GsonBuilder().create();

        Klass klass = gson.fromJson(JSON_TEXT, Klass.class);

        assertEquals(TEXT, klass.text);
        assertEquals(NUMBER, klass.anInt);

        System.out.println(klass.toString());
    }

    @Test
    public void serialize() {
        Gson gson = new GsonBuilder().create();

        JsonObject except = new JsonObject();
        except.addProperty("TEXT", "a");
        except.addProperty("integer", 1);

        Klass klass = new Klass();
        JsonElement jsonElement = gson.toJsonTree(klass);

        assertEquals(except, jsonElement);

    }
}
