import React from 'react';
import { Pressable, StyleSheet, Text, useWindowDimensions, View } from 'react-native';

export function NeobrutalismNativeButton({ onPress }: { onPress?: () => void }) {
  const compact = useWindowDimensions().width < 600;
  return (
    <View style={[styles.card, compact && styles.compact]}>
      <Text style={styles.title}>Bold action</Text>
      <Text style={styles.body}>Hard borders and offsets stay explicit across states.</Text>
      <Pressable accessibilityRole="button" accessibilityState={{ disabled: !onPress }} disabled={!onPress} onPress={onPress} style={({ pressed }) => [styles.button, pressed && styles.pressed]}>
        <Text style={styles.label}>Launch</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  card: { padding: 20, borderWidth: 3, borderColor: '#111', backgroundColor: '#ffd84d' },
  compact: { padding: 16 },
  title: { fontSize: 22, fontWeight: '900', color: '#111' },
  body: { marginTop: 8, color: '#111' },
  button: { marginTop: 18, minHeight: 48, paddingHorizontal: 18, justifyContent: 'center', borderWidth: 3, borderColor: '#111', borderRadius: 0, backgroundColor: '#ff6b6b', shadowColor: '#111', shadowOpacity: 1, shadowRadius: 0, shadowOffset: { width: 5, height: 5 }, elevation: 5 },
  pressed: { transform: [{ translateX: 3 }, { translateY: 3 }], shadowOpacity: 0 },
  label: { textAlign: 'center', fontWeight: '900', color: '#111' },
});

// Verification: explicit border/state, semantic Pressable, compact adaptation, deterministic shadow-free pressed state.
// Fallback: remove offset shadow while retaining border, fill, target size, and state.
