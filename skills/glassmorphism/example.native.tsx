import React from 'react';
import { Pressable, StyleSheet, Text, useWindowDimensions, View } from 'react-native';

export function GlassmorphismNativeCard({ onPress }: { onPress?: () => void }) {
  const compact = useWindowDimensions().width < 600;
  return (
    <View style={[styles.backdrop, compact && styles.compact]}>
      <View style={styles.glass}>
        <Text style={styles.title}>Frosted panel</Text>
        <Text style={styles.body}>Blur is optional. Tint, border, focus, and state remain usable without it.</Text>
        <Pressable accessibilityRole="button" accessibilityState={{ disabled: !onPress }} disabled={!onPress} onPress={onPress} style={({ pressed }) => [styles.button, pressed && styles.pressed]}>
          <Text style={styles.label}>Open</Text>
        </Pressable>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  backdrop: { padding: 20, backgroundColor: '#66728f' },
  compact: { padding: 16 },
  glass: { padding: 20, borderRadius: 22, borderWidth: 1, borderColor: 'rgba(255,255,255,0.55)', backgroundColor: 'rgba(255,255,255,0.78)', shadowColor: '#000', shadowOpacity: 0.16, shadowRadius: 8, shadowOffset: { width: 0, height: 4 } },
  title: { fontSize: 20, fontWeight: '700' },
  body: { marginTop: 8, color: '#20242c' },
  button: { marginTop: 16, minHeight: 48, paddingHorizontal: 18, justifyContent: 'center', borderRadius: 16, borderWidth: 1, borderColor: '#3f4a60', backgroundColor: 'rgba(255,255,255,0.62)' },
  pressed: { opacity: 0.75 },
  label: { textAlign: 'center', fontWeight: '700' },
});

// Verification: bounded glass shell, native Pressable, compact adaptation, explicit state.
// Fallback: opaque tinted surface when blur/translucency is unavailable or disabled.
