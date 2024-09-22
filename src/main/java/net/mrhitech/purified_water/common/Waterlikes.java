package net.mrhitech.purified_water.common;

import java.util.Locale;

public enum Waterlikes {
    
    PURIFIED_WATER(-12618011);
    
    private final int color;
    private final String id;
    
    
    Waterlikes(int color) {
        this.id = this.name().toLowerCase(Locale.ROOT);
        this.color = color;
    }
    
    public String getId() {
        return id;
    }
    
    public int getColor() {
        return color;
    }
    
}